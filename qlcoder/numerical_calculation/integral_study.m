function y =f(t)
  y = sqrt((750*(3*t^2-4*t+1)+1500*t^2)^2+((-300)*(1-t)^2+900*((-3)*t^2+2*t)+1500*t^2)^2)
endfunction

[q, ier, nfun, err] = quad ("f", 0, 1)  