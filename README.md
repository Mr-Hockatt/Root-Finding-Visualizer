# Root-Finding-Visualizer
Implementation of root-finding algorithms for polynomials, with numerical solutions and visualization.</br>
This project was created as part of my <b>Mathematical Methods</b> class on my 4th semester of Mechatronics Engineering.

![plot](https://user-images.githubusercontent.com/53312754/120087491-31f64e00-c0ae-11eb-9ce1-441ba715b39f.png)


## Features
<ul>
  <li>Numerical solution by both <a href="https://en.wikipedia.org/wiki/Bisection_method">Bisection</a> and <a href="https://en.wikipedia.org/wiki/Newton%27s_method">Newton-Raphson</a> methods</li>
  <li>Data visualization of the polynomial</li>
  <li>Table presentation of the numerical solution by the selected method</li>
  <li>CSV storage of the numerical solution</li>
</ul>

The main window is a simple GUI created with Tkinter and the plotting happens with Matplotlib. The spinbox allows the selection of the polynomial's order. As selected, small boxes will appear above, each one to input the coefficients for each of the powers on the polynomial. Click the "Generar P(x)" to generate the polynomial, then proceed with the method selection.

![gui](https://user-images.githubusercontent.com/53312754/120087586-d4163600-c0ae-11eb-9c30-80a55b8317e7.jpg)

The table shows a preview of the numerical solution of the root-finding. Complete data is stored on a .csv file for whatever purposes needed.

![table](https://user-images.githubusercontent.com/53312754/120087603-ebedba00-c0ae-11eb-9584-b0ec864f75f8.jpg)

## Requirements
<ul>
  <li><b>CSV</b></li>
  <li><b>Matplotlib</b></li>
  <li><b>Numpy</b></li>
  <li><b>Tkinter</b></li>
</ul>
