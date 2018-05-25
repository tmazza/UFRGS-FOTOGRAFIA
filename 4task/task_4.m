close all;
clear all;

A = imread('./cameraman.tif');
[M,N] = size(A);


% multiple -1^(x+y) space domain
I0 = zeros(M, N);
for x = 1:M
    for y = 1:N
        I0(x, y) = (-1)^(x+y) * A(x,y);
    end
end

% fftshift frequency domain
f = fft2(double(A));
I1 = ifft2(fftshift(f));

% multiple -1^(x+y) frequency domain
[M,N] = size(A);
g = zeros(M, N);
for x = 1:M
    for y = 1:N
        g(x, y) = (-1)^(x+y) * f(x,y);
    end
end
I2 = ifft2(g);

% fftshift space domain
I3 = fftshift(A);


subplot(2, 2, 1), imshow(I0, []), title("multiple -1^(x+y) space domain");
subplot(2, 2, 2), imshow(I1, []), title("fftshift frequency domain");
subplot(2, 2, 3), imshow(I2, []), title("multiple -1**(x+y) frequency domain");
subplot(2, 2, 4), imshow(I3, []), title("fftshift space domain");