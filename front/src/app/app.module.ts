import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { AddDocumentsComponent } from './components/add-documents/add-documents.component';
import { UpdateDocumentsComponent } from './components/update-documents/update-documents.component';
import { ViewDocumentsComponent } from './components/view-documents/view-documents.component';
import { HttpClientModule } from "@angular/common/http"
import { ReactiveFormsModule } from '@angular/forms';
import { UpdateSignersComponent } from './components/update-signers/update-signers.component';

@NgModule({
  declarations: [
    AppComponent,
    AddDocumentsComponent,
    UpdateDocumentsComponent,
    ViewDocumentsComponent,
    UpdateSignersComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    ReactiveFormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
