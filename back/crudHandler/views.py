from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from crudHandler.models import Company, Documents, Signers
from crudHandler.serializers import CompanySerializer, DocumentsSerializer, SignersSerializer

import requests

@csrf_exempt
def companyApi(request,id=0):
    if request.method == 'GET':
        company = Company.objects.all()
        company_serializer = CompanySerializer(company, many=True)
        return JsonResponse(company_serializer.data, safe=False)
    
    elif request.method == 'POST':
        company_data = JSONParser().parse(request)
        company_serializer = CompanySerializer(data=company_data)
        if company_serializer.is_valid():
            company_serializer.save()
            return JsonResponse("DEBUG: COMPANY - POST - Certo!", safe=False)
        return JsonResponse("DEBUG: COMPANY - POST - Erro")
    
    elif request.method == 'PUT':
        company_data = JSONParser().parse(request)
        company = Company.objects.get(company_ID=company_data['company_ID'])
        company_serializer=CompanySerializer(company,data=company_data)
        if company_serializer.is_valid():
            company_serializer.save()
            return JsonResponse("DEBUG: COMPANY - PUT - Certo!", safe=False)
        return JsonResponse("DEBUG: COMPANY - PUT - Erro")
    
    elif request.method == 'DELETE':
        company = Company.objects.get(company_ID=id)
        company = company.delete()
        return JsonResponse("DEBUG: COMPANY - DELETE - Certo!", safe = False)

@csrf_exempt    
def documentsApi(request,id=0):
    if request.method == 'GET':
        if id==0:
            documents = Documents.objects.all()
            documents_serializer = DocumentsSerializer(documents, many=True)
            return JsonResponse(documents_serializer.data, safe=False)
        else:
            print("esse é o id: ",id)
            documents = Documents.objects.get(documents_ID=id)
            documents_serializer = DocumentsSerializer(documents)
            return JsonResponse(documents_serializer.data, safe=False)
    
    elif request.method == 'POST':
        documents_data = JSONParser().parse(request)
        apiResponseData = makeAPIrequest(documents_data)
        signers_data = signerData(apiResponseData)

        documents_serializer = DocumentsSerializer(data = apiResponseData)
        if documents_serializer.is_valid():

            temp_documents_open_id = documents_serializer.validated_data['open_id']
            documents_serializer.save()
            temp_documents = Documents.objects.get(open_id=temp_documents_open_id)
            signers_data[0]['documentID'] = int(temp_documents.documents_ID)
            signers_serializer = SignersSerializer(data = signers_data, many=True)

            if signers_serializer.is_valid():
                signers_serializer.save()
                return JsonResponse(temp_documents.documents_ID, safe=False)
            return JsonResponse("DEBUG: DOCUMENT - POST - SIGNER - Erro")
        return JsonResponse("DEBUG: DOCUMENT - POST - Erro")
    
    elif request.method == 'PUT':
        documents_data = JSONParser().parse(request)
        documents = Documents.objects.get(documents_ID=documents_data['documents_ID'])
        documents_serializer=DocumentsSerializer(documents,data=documents_data)
        if documents_serializer.is_valid():
            documents_serializer.save()
            return JsonResponse("DEBUG: DOCUMENT - PUT - Certo!", safe=False)
        return JsonResponse("DEBUG: DOCUMENT - PUT - Erro")
    
    elif request.method == 'DELETE':
        documents = Documents.objects.get(documents_ID=id)
        documents = documents.delete()
        return JsonResponse("DEBUG: DOCUMENT - DELETE - Certo!", safe = False)
    
@csrf_exempt    
def signersApi(request,id=0):
    if request.method == 'GET':
        if id==0:
            signers = Signers.objects.all()
            signers_serializer = SignersSerializer(signers, many=True)
            return JsonResponse(signers_serializer.data, safe=False)
        else:
            signers = Signers.objects.get(signers_ID=id)
            signers_serializer = SignersSerializer(signers)
            return JsonResponse(signers_serializer.data, safe=False)
    
    elif request.method == 'POST':
        signers_data = JSONParser().parse(request)
        signers_serializer = SignersSerializer(data=signers_data)
        if signers_serializer.is_valid():
            signers_serializer.save()
            return JsonResponse("DEBUG: SIGNER - POST - Certo!", safe=False)
        return JsonResponse("DEBUG: SIGNER - POST - Erro", safe=False)
    
    elif request.method == 'PUT':
        signers_data = JSONParser().parse(request)
        signers = Signers.objects.get(signers_ID=signers_data['signers_ID'])
        signers_serializer=SignersSerializer(signers,data=signers_data)
        if signers_serializer.is_valid():
            signers_serializer.save()
            return JsonResponse("DEBUG: SIGNER - PUT - Certo!", safe=False)
        return JsonResponse("DEBUG: SIGNER - PUT - Erro", safe=False)
    
    elif request.method == 'DELETE':
        signers = Signers.objects.get(signers_ID=id)
        signers = signers.delete()
        return JsonResponse("DEBUG: SIGNER - DELETE - Certo!", safe = False)

def documents_signersApi(request):
    if request.method == 'GET':
        signers = Signers.objects.all()
        documents = Documents.objects.all()
        signers_documents = []
        for signer in signers:
            for document in documents:
                if signer.documentID_id == document.documents_ID:
                    signer_documents = {
                        "signer_name": signer.name,
                        "signer_email": signer.email,
                        "signers_ID": signer.signers_ID,
                        "document_ID": document.documents_ID,
                        "document_name": document.name,
                        "document_url": document.url
                    }
                    signers_documents.append(signer_documents)
                    break
        return JsonResponse(signers_documents, safe=False)

    
def makeAPIrequest(body):
    print("esse é o body: ", body)
    tempCompanyID = int(body.get('companyID'))
    tempUrl = body.get('url_pdf')

    url = "https://sandbox.api.zapsign.com.br/api/v1/docs/"
    headers = {'Authorization': 'Bearer 8ac47fd2-65b1-4542-82d8-e11a64d9c13f05104f5b-3c9e-4258-b0c1-7acaf09bbc3b'}
    response = requests.post(url, headers=headers, json=body, verify=False)
    response_data = response.json()

    response_data['companyID'] = tempCompanyID
    response_data['url'] = tempUrl
    return response_data

def signerData(response):
    only_email = response['created_by']['email']
    response['created_by'] = only_email

    return response.pop('signers', [])