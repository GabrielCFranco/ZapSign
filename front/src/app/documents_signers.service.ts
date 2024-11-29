import { Injectable } from '@angular/core';
import Documents from './Documents';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class Documents_SignersService {
  private url: string = "http://127.0.0.1:8000/crudHandler/"
  constructor(private http: HttpClient) { }

  getDocuments_Signers(): Observable<Documents[]> {
    return this.http.get<Documents[]>(`${this.url}documents_signers/`)
  }
}
