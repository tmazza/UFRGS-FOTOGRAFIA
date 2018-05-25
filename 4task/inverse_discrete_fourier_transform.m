function I = inverse_discrete_fourier_transform(F)
  [M, N] = size(F);
  e = exp(1);
  
  I = zeros(M, N);
  for x = 0:M-1
     for y = 0:N-1
         
        sum = 0;
        for u = 0:M-1
          for v = 0:N-1
            theta = 2*pi*( (u*x)/M + (v*y)/N );
            sum = sum + F(u+1, v+1)*(cos(theta) + 1i * sin(theta));
          end
        end
        I(x+1, y+1) = (1/(M*N)) * sum;
        
     end
  end
  
  I = real(I)
  
end