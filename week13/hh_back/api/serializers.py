from rest_framework import serializers
from api.models import Company, Vacancy


class CompanySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    city = serializers.CharField()
    address = serializers.CharField()

    def create(self, validated_data):
        company = Company()
        company.name = validated_data.get('name')
        company.description = validated_data.get('description')
        company.city = validated_data.get('city')
        company.address=validated_data.get('address')

        company.save()
        return company

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.description = validated_data.get('description')
        instance.city = validated_data.get('city')
        instance.address = validated_data.get('address')
        instance.save()
        return instance


class VacancySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    salary = serializers.FloatField()
    company = CompanySerializer(read_only=1)
    #company = serializers.IntegerField(write_only=True)

    class Meta:
        model = Vacancy
        fields = ('id', 'name', 'description', 'salary', 'company')

    # def create(self, validated_data):
    #     vacancy = Vacancy()
    #     vacancy.name = validated_data.get('name')
    #     vacancy.description = validated_data.get('description')
    #     vacancy.salary = validated_data.get('salary')
    #     vacancy.company = validated_data.get('company')
    #     vacancy.save()
    #     return vacancy
    #
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name')
    #     instance.description = validated_data.get('description')
    #     instance.salary = validated_data.get('salary')
    #     instance.vacancy = validated_data.get('company')
    #     instance.save()
    #     return instance
