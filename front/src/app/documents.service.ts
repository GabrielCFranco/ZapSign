import { Injectable } from '@angular/core';
import Documents from './Documents';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DocumentsService {
  private url: string = "http://127.0.0.1:8000/crudHandler/"
  constructor(private http: HttpClient) { }

  getDocuments(): Observable<Documents[]> {
    return this.http.get<Documents[]>(`${this.url}documents/`)
  }
  
  getDocumentsById(id: number): Observable<Documents[]> {
    return this.http.get<Documents[]>(`${this.url}documents/${id}`)
  }

  addDocuments(documents: Documents): Observable<Documents[]>{
    console.log("isso é o documents:",documents)
    return this.http.post<Documents[]>(`${this.url}documents/`, documents)
  }

  updateDocuments(id: number, documents: Documents): Observable<Documents>{
    return this.http.put<Documents>(`${this.url}documents/${id}`, documents)
  }
  
  deleteDocuments(id: number): Observable<Documents> {
    return this.http.delete<Documents>(`${this.url}documents/${id}`)
  }
}
