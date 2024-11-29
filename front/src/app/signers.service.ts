import { Injectable } from '@angular/core';
import Signers from './Signers';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SignersService {
  private url: string = "http://127.0.0.1:8000/crudHandler/"
  constructor(private http: HttpClient) { }

  getSigners(): Observable<Signers[]> {
    return this.http.get<Signers[]>(`${this.url}signers/`)
  }

  getSignersById(id: number): Observable<Signers[]> {
    return this.http.get<Signers[]>(`${this.url}signers/${id}`)
  }
  
  updateSigners(id: number, signers: Signers): Observable<Signers[]> {
    return this.http.put<Signers[]>(`${this.url}signers/${id}`, signers)
  }

  deleteSigners(id: number): Observable<Signers> {
    return this.http.delete<Signers>(`${this.url}signers/${id}`)
  }
}
