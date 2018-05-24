% Comparação de resultados matlab e funções criadas
A = imread('./cameraman.tif');

F = fft2(double(A));

R = ifft2(real(F));
I = ifft2(complex(0, imag(F)));

SOMA = ifft2(real(F) + complex(0, imag(F)));

subplot(2,2,1), imshow(R, []), title("Parte real");
subplot(2,2,2), imshow(I, []), title("Parte imaginária");
subplot(2,2,3), imshow(SOMA, []), title("Soma real+imaginária");