from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Customer, Profession, DataSheet, Document


class DataSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSheet
        fields = ("id", "description", "historical_data")


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ("id", "description")


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ("id", "dtype", "doc_number", "customer")


class CustomerSerializer(serializers.ModelSerializer):
    num_professions = serializers.SerializerMethodField()
    data_sheet = DataSheetSerializer(read_only=True)
    profession = ProfessionSerializer(many=True)
    document_set = DocumentSerializer(many=True)

    class Meta:
        model = Customer
        fields = ("id", "name", "address", "profession", "data_sheet", "active",
                  "status_message", "num_professions", "document_set")

    def create(self, validated_data):
        professions = validated_data["profession"]
        del validated_data["profession"]

        document_set = validated_data["document_set"]
        del validated_data["document_set"]

        data_sheet = validated_data["data_sheet"]
        del validated_data["data_sheet"]

        customer = Customer.objects.create(**validated_data)
        d_sheet = DataSheet.objects.create(**data_sheet)
        customer.data_sheet = d_sheet

        for doc in document_set:
            Document.objects.create(
                dtype=doc["dtype"],
                doc_number=doc["doc_number"],
                customer_id=customer.id
            )

        for profession in professions:
            prof = Profession.objects.create(**profession)
            customer.professions.add(prof)

        customer.save()

        return customer

    def get_num_professions(self, obj):
        return obj.num_professions()

    def get_data_sheet(self, obj):
        return obj.data_sheet.description


