clear; clc;
load('D:\double_check\info\stat_results\BetaX2');
B_I = [];
% plot beta_x - beta_x-1
figure; hold on;
for idx = 2 : 5
    R = BetaX2(:, idx) - BetaX2(:, idx-1);
    R=R(R>0);
    [m, n] = hist(R, 20);
    plot(n, m/sum(m));
end
figure;
plot([-2e-3 16e-3], [-2e-3 16e-3], 'k--');
x = BetaX2(:, 2) - BetaX2(:, 1);
y1 = BetaX2(:, 3) - BetaX2(:, 2); 
y2 = BetaX2(:, 4) - BetaX2(:, 3);
y3 = BetaX2(:, 5) - BetaX2(:, 4); 
loglog(x, y1, 'o'); hold on;
loglog(x, y2, 'o');
loglog(x, y3, 'o');