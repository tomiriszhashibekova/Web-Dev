import { Injectable } from '@angular/core';
import {Observable, of} from 'rxjs';
import {CATEGORIES, Category} from './categories';
import {Job, Jobs} from './jobs';

@Injectable({
  providedIn: 'root'
})
export class CategoryService {

  getCategories(): Observable<Category[]> {
    return of(CATEGORIES);
  }
  getCategory(id: number): Observable<Category> {
    return of(CATEGORIES.find(category => category.id === id));
  }

  getCategoryProducts(id: number): Observable<Job[]> {
    return of(Jobs.filter(product => product.id === (CATEGORIES.find(category => category.id === id).id)));
  }

  getProduct(id: number): Observable<Job> {
    return of(Jobs.find(product => product.id === id));
  }


  constructor() { }
}
