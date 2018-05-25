function F = discrete_fourier_transform(A)
  [M, N] = size(A);
  e = exp(1);  
  F = zeros(M, N);
  for u = 0:M-1
     for v = 0:N-1
         
        sum = 0;
        for x = 0:M-1
          for y = 0:N-1
            theta = 2*pi*( (u*x)/M + (v*y)/N );
            sum = sum + A(x+1, y+1) * (cos(theta) - 1i*sin(theta));
          end
        end
        F(u+1, v+1) = sum;
        
     end
  end
end

