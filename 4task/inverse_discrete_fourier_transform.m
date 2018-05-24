function I = inverse_discrete_fourier_transform(F)
  [M, N] = size(F);
  e = exp(1);
  
  I = zeros(M, N);
  for x = 0:M-1
     for y = 0:N-1
         
        sum = 0;
        for u = 0:M-1
          for v = 0:N-1
            sum = sum + F(u+1, v+1) * (e ^ (1i*2*pi*( (u*x)/M + (v*y)/N )));
          end
        end
        I(x+1, y+1) = (1/(M*N)) * sum;
        
     end
  end
  
  I = real(I)
  
end