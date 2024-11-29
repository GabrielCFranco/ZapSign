import { Component } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { DocumentsService } from 'src/app/documents.service';

@Component({
  selector: 'app-update-documents',
  templateUrl: './update-documents.component.html',
  styleUrls: ['./update-documents.component.css']
})
export class UpdateDocumentsComponent {
  
  documents?: any
  data: any
  constructor(private documentsService: DocumentsService, private route: ActivatedRoute, private router : Router) { }
  
  ngOnInit(): void {
    let id = this.route.snapshot.params['id'];
    this.documentsService.getDocumentsById(id).subscribe(data => {
      this.documents = data
      console.log(this.documents)
    })
  }

  form = new FormGroup({
    name:         new FormControl('', Validators.required),
    url:          new FormControl('', Validators.required)
  });

  submit(){
    this.data = this.form.value
    this.documents.name = this.data.name
    this.documents.email = this.data.email
    console.log(this.data)
    
    this.documentsService.updateDocuments(this.route.snapshot.params['id'], this.documents).subscribe(data => {
      console.log(data)
    })

    this.router.navigate(['/']);
  }
}
