% Comparação resultados matlab e funções criadas

A = imread('./cameraman_small.tif');
F = fft2(double(A));
F_custom = discrete_fourier_transform(double(A));

a = inverse_discrete_fourier_transform(F);
b = ifft2(F_custom);
c = inverse_discrete_fourier_transform(F);

subplot(2,2,1), imshow(A, []), title("Original");
subplot(2,2,2), imshow(a, []), title("fft + custom idft");
subplot(2,2,3), imshow(b, []), title("custom dft + ifft");
subplot(2,2,4), imshow(c, []), title("custom dft + custom idft");