function our_model()
clear; clc;
beta = load('D:\Projects\Pycharm\SIR\master\data\stat_empirical\beta_idd_2_mdf');
beta = beta(7, 2:end);
x = 1 : 29;
b = 0.1835; c = 0.001186; beta_x = beta(1);
beta_x = [beta_x beta(1)+cumsum(c*exp(-b*x))];
p_x = 1 - cumprod(1-beta_x);

%--按照标准SIR，由p_x来估计beta
x = 1 : 30; u1 = dot(x, log(1-p_x)); v1 = dot(x, x); h1 = u1/v1;
beta_est1 = 1 - exp(h1);
p_x_est = real(1 - exp(x.*h1));
%--真实信息：4139280772802348
s = 'D:\Projects\Pycharm\SIR\Data\45\4139280772802348\res\';
load(strcat(s, 'N1')); load(strcat(s, 'N3'));
res = [];
for i = 1 : 1000
    res = [res N3(i)/sum(N1(i: length(N1)))];
end
idx = find(res~=0&res~=1&~isnan(res));
x = idx-1; y = res(idx); x = x(1:30); y = y(1:30);
u2 = dot(x, log(1-y)); v2 = dot(x, x); h2 = u2/v2;
beta_est2 = 1 - exp(h2);
p_true_est = real(1 - exp(x.*h2));

figure(); 
h1 = plot([0 0.15], [0 0.15], 'k--', 'LineWidth', 2); hold on; 
h2 = plot(p_x_est, p_x, '-', 'Color', 'g', 'LineWidth', 4);
h3 = plot(p_true_est, y, 'd', 'MarkerSize', 10, 'MarkerEdgeColor', [0.85, 0.33, 0.1], 'MarkerFaceColor', [0.85, 0.33, 0.1]);
h4 = plot(p_x, y, 'v', 'MarkerSize', 7, 'MarkerEdgeColor', [0.1, 0.5, 0.1], 'MarkerFaceColor', [0.1, 0.5, 0.1]);
xlabel('$\hat{P(t)}$', 'Interpreter', 'LaTex', 'FontSize', 18);
ylabel('$P(t)$', 'Interpreter', 'LaTex', 'FontSize', 18);
legend([h3, h2, h1], ...
    '$Empirical$', ...
    '$Our\ Model$', ...
    '$DiagnalLine$', ...
    'location', 'NW');
xlim([0 0.15]); ylim([0 0.15]);
set(gca, 'FontName', 'Times New Roman', 'FontSize', 18);
set(legend, 'FontName', 'Times New Roman', 'FontSize', 15, 'Interpreter', 'latex', 'Box', 'Off');
set(gca, 'LineWidth', 2);
set(gcf,'color','white');
set(gcf, 'Position', [600 400 700 500]);



