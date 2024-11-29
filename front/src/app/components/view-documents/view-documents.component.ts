import { Component } from '@angular/core';
import { DocumentsService } from 'src/app/documents.service';
import { SignersService } from 'src/app/signers.service';
import { Documents_SignersService } from 'src/app/documents_signers.service'
import { Router } from '@angular/router';

@Component({
  selector: 'app-view-documents',
  templateUrl: './view-documents.component.html',
  styleUrls: ['./view-documents.component.css']
})
export class ViewDocumentsComponent {
  documents: any | undefined
  signers: any | undefined
  documents_signers: any[] = [] 
  documents_signers2: any
  documentsLoaded = false;
  signersLoaded = false;
  constructor(private documentService: DocumentsService, private signersService: SignersService, private document_signerService: Documents_SignersService , private router: Router){}

  ngOnInit(): void {
    this.document_signerService.getDocuments_Signers().subscribe(data=> {
      this.documents_signers2 = data;
    })
  }

  deleteDocuments(id: number){
    this.documentService.deleteDocuments(id).subscribe(data => {
      this.ngOnInit();
    })
  }
  logDocumentInfo(docs_sigs: any): void {
  }
}
