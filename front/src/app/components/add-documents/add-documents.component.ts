import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { DocumentsService } from 'src/app/documents.service';
import Signers from 'src/app/Signers';

@Component({
  selector: 'app-add-documents',
  templateUrl: './add-documents.component.html',
  styleUrls: ['./add-documents.component.css']
})
export class AddDocumentsComponent implements OnInit {
  constructor(private documentsService: DocumentsService, private router: Router) {}

  ngOnInit(): void {}

  data: any;
  signers: Signers[] = [];

  form = new FormGroup({
    name:         new FormControl('', Validators.required),
    signers_name: new FormControl('', Validators.required),
    signers_email:new FormControl('', Validators.required),
    url:          new FormControl('', Validators.required),
    companyID:   new FormControl('', Validators.required)
  });

  addDocuments(): void {
    this.signers = [
      {
        name: this.form.value.signers_name!,
        email: this.form.value.signers_email!
      }
    ];

    const documentsData = {
      name: this.form.value.name,
      url_pdf: this.form.value.url,
      signers: this.signers,
      companyID: this.form.value.companyID
    };
    this.data = documentsData;
    this.documentsService.addDocuments(this.data).subscribe({
      next: (response) => {
        this.router.navigate(['/']);
      },
      error: (err) => {
        console.error('Error while adding document:', err);
      }
    });
  }
}
