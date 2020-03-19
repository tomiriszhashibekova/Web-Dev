import { Component, OnInit } from '@angular/core';
import {Category} from '../categories';
import {ActivatedRoute} from '@angular/router';
import {CategoryService} from '../category.service';

import {Job} from '../jobs';
import { Location } from '@angular/common';

@Component({
  selector: 'app-category-detail',
  templateUrl: './category-detail.component.html',
  styleUrls: ['./category-detail.component.css']
})
export class CategoryDetailComponent implements OnInit {

  products: Job[];
  category: Category;

  constructor(
    private route: ActivatedRoute,
    private categoryService: CategoryService,
    private location: Location) { }
    getCategoryProducts(): void {
      const id = +this.route.snapshot.paramMap.get('categoryId');
      this.categoryService.getCategoryProducts(id)
        .subscribe(products => this.products = products);
      this.categoryService.getCategory(id)
        .subscribe(category => this.category = category);
    }
  
  ngOnInit(): void {
    this.getCategoryProducts();
  }
  goBack(): void {
    this.location.back();
  }

}
