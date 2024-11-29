import { Component } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { SignersService } from 'src/app/signers.service';

@Component({
  selector: 'app-update-signers',
  templateUrl: './update-signers.component.html',
  styleUrls: ['./update-signers.component.css']
})
export class UpdateSignersComponent {
  signer?: any
  data: any
  constructor(private signersService: SignersService, private route: ActivatedRoute, private router : Router) { }
  
  ngOnInit(): void {
    let id = this.route.snapshot.params['id'];
    this.signersService.getSignersById(id).subscribe(data => {
      this.signer = data
      console.log(this.signer)
    })
  }

  form = new FormGroup({
    signers_name:           new FormControl('', Validators.required),
    signers_email:          new FormControl('', Validators.required)
  });

  submit(){
    this.data = this.form.value
    this.signer.name = this.data.signers_name
    this.signer.email = this.data.signers_email
    console.log(this.data)
    
    this.signersService.updateSigners(this.route.snapshot.params['id'], this.signer).subscribe(data => {
      console.log(data)
    })

    this.router.navigate(['/']);
  }
}
