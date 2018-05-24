function F = discrete_fourier_transform(A)
  [M, N] = size(A);
  e = exp(1);  
  F = zeros(M, N);
  for u = 0:M-1
     for v = 0:N-1
         
        sum = 0;
        for x = 0:M-1
          for y = 0:N-1
            sum = sum + A(x+1, y+1) * (e^(-1i*2*pi*( (u*x)/M + (v*y)/N )));
          end
        end
        F(u+1, v+1) = sum;
        
     end
  end
end

