% Transformada de fourier cálculada a partir 
% das funções do matlab e transformada inversa ambém

A = imread('./cameraman_small.tif');

F = discrete_fourier_transform(double(A));
I = inverse_discrete_fourier_transform(F);

subplot(1,2,1), imshow(A, []), title("Original");
subplot(1,2,2), imshow(I, []), title("Reconstrução");