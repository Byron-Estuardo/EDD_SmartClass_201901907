import { Component, OnInit } from '@angular/core';
import { Title } from '@angular/platform-browser';
import { Router } from '@angular/router';

@Component({
  selector: 'app-estudiante-v',
  templateUrl: './estudiante-v.component.html',
  styleUrls: ['./estudiante-v.component.css']
})
export class EstudianteVComponent implements OnInit {

  constructor(private title: Title, private router: Router) { }

  logout(){
    var data = JSON.stringify({
        "carnet": 0
      });

      fetch('http://localhost:3000/LogOut', {
        method: 'post',
        headers: {
          'Content-Type': 'application/json'
        },
        body: data

      })
      .then(response => response.json())

      this.router.navigate(['/']);
    }


  ngOnInit(): void {
    this.title.setTitle('Usuario');
  }

}
