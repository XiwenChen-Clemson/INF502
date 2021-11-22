CPSC-6040

XIWEN CHEN (xiwenc@g.clemson.edu)
Assignment #7  Tone Mapping

### overall
- Implement Tone mapping by gamma compression, linear filtering, Bilateral filtering

### Complie
```
make
```
### how to run
- ``` ./main in.hdr ``` Then,
  -  press ```1``` for simple tone mapping. The Console will ask you for the value of gamma (0-1);
  -  press ```2``` for tone mapping by box filtering. The Console will ask you for the value of kernel size (odd value), and taget range (1-5 would be good);
  -  press ```3``` for tone mapping by bilateral filtering. The Console will ask you for the value of kernel size (odd value), sigamal of spatial kernel, sigamal of range kernel; and taget range (1-5 would be good).
  -  press ```o``` or ```O``` to recovery the processed image to orignal hdr image (e.g, when after you press ```1``` to do simple tone mapping, you can press ```o``` to recovery the image and then use other methods to reprocess the hdr image); 
  -  press ```w``` for writing the image to file.



### Some paras
- ```kernel size =5```
- ```sigma_s = 5``` and ```sigma_r = 0.5```

