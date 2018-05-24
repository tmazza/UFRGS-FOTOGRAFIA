% Transformada de fourier cálculada a partir 
% das funções do matlab e transformada inversa
% realizada com função criada.

A = imread('./cameraman_small.tif');

F = fft2(double(A));
I = inverse_discrete_fourier_transform(F);

subplot(1,2,1), imshow(A, []), title("Original");
subplot(1,2,2), imshow(I, []), title("Reconstrução");