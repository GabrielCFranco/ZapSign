import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ViewDocumentsComponent } from './components/view-documents/view-documents.component';
import { AddDocumentsComponent } from './components/add-documents/add-documents.component';
import { UpdateDocumentsComponent } from './components/update-documents/update-documents.component';
import { UpdateSignersComponent } from './components/update-signers/update-signers.component';
const routes: Routes = [
  { path: '', component: ViewDocumentsComponent },
  { path: 'add', component: AddDocumentsComponent },
  { path: 'updateDoc/:id', component: UpdateDocumentsComponent},
  { path: 'updateSig/:id', component: UpdateSignersComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
