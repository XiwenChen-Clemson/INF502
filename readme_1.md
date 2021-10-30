CPSC-6040

XIWEN CHEN (xiwenc@g.clemson.edu)
Assignment #5  image transformation

### overall
- Searh the size of output image by forward mapping.
- Do transformation by inverse mapping.



### Complie
```
make
```
### how to run

```./warper in.ong [out.png] ``` Please press ``` w ``` to store the image


### Functions
- rotation:``` r theta```
- scale:``` s sx sy```
- translate: ```t dx dy```
- shear:``` h hx hy```
- flip: fx = 1 flip horizontally, fy = 1 flip vertically: ```f fx fy```
- perspective: ```p px py```
- nonlinear twirl warp: ```n cx cy s```
- nonlinear ripple warp: ```m tx ty ax ay```
- ```d``` done



### Issues
Some values are not worked and may result in image distortion.


