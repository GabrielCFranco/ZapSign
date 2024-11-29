from rest_framework import serializers
from crudHandler.models import Company, Documents, Signers

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('company_ID',
                  'name',
                  'created_at',
                  'last_updated_at',
                  'api_token')

class DocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = ('documents_ID',
                  'open_id',
                  'token',
                  'name',
                  'url',
                  'status',
                  'created_at',
                  'last_updated_at',
                  'created_by',
                  'companyID',
                  'externalID')
        
class SignersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signers
        fields = ('signers_ID',
                  'token',
                  'status',
                  'name',
                  'email',
                  'externalID',
                  'documentID')