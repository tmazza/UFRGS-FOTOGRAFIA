close all;
clear all;

A = imread('./cameraman.tif');
f = fft2(double(A));

amplitude = log(abs(f));
angles = angle(f);
[M,N] = size(A);
phase = zeros(M, N);
for x = 1:M
    for y = 1:N
        phase(x, y) = exp(1)^(1i*angles(x,y));
    end
end
phase = ifft2(phase);


subplot(1, 2, 1), imshow(amplitude, []), title("Amplitude");
subplot(1, 2, 2), imshow(phase, []), title("Phase");