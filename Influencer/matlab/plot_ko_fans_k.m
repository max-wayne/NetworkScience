function plot_ko_fans_k()
fig = figure;
left_color = [0 0 0];
right_color = [0 0 0];
set(fig,'defaultAxesColorOrder',[left_color; right_color]);

s = 'D:/Projects/Pycharm/BIGV/data/bigv/ko_fans_fans/';
avg_fans_fans = []; median_fans_fans = []; idx = [];
for i = 18 : 26
    idx = [idx 2^i];
    s1 = strcat(s, num2str(i));
    data1 = load(s1);
    avg_fans_fans = [avg_fans_fans mean(data1)];
%     median_fans_fans = [median_fans_fans median(data1)];
end
yyaxis left
h1 = semilogx(idx, avg_fans_fans, '--o', 'LineWidth', 1, 'Color', [0, 0.45, 0.74], 'MarkerSize', 10, 'MarkerEdgeColor', [0, 0.45, 0.74], 'MarkerFaceColor', [0, 0.45, 0.74]);
hold on
% h2 = loglog(idx, median_fans_fans, '--o', 'LineWidth', 1, 'Color', [.85, .33, .1], 'MarkerSize', 10, 'MarkerEdgeColor', [.85, .33, .1], 'MarkerFaceColor', [.85, .33, .1]);
xlabel('$K_{o}$', 'interpreter', 'Latex');
ylabel('$fans\_fans$', 'interpreter', 'Latex');
% ylim([10, 1e4]);
set(gca, 'FontSize', 18);
set(gca, 'LineWidth', 2);
set(gcf,'color','white');
set(gcf, 'Position', [600 400 700 500]);

t = 'D:/Projects/Pycharm/BIGV/data/bigv/ko_fans_fos/';
avg_fans_fos = []; median_fans_fos = []; idx = [];
for i = 18 : 26
    idx = [idx 2^i];
    t1 = strcat(t, num2str(i));
    data2 = load(t1);
    avg_fans_fos = [avg_fans_fos mean(data2)];
%     median_fans_fos = [median_fans_fos median(data2)];
end
yyaxis right
h3 = semilogx(idx, avg_fans_fos, '--d', 'LineWidth', 1, 'Color', 'r', 'MarkerSize', 10, 'MarkerEdgeColor', 'r', 'MarkerFaceColor', 'r');
% h4 = loglog(idx, median_fans_fos, '--d', 'LineWidth', 1, 'Color', [.25, .25, .25], 'MarkerSize', 10, 'MarkerEdgeColor', [.25, .25, .25], 'MarkerFaceColor', [.25, .25, .25]);
ylabel('$fans\_friends$', 'interpreter', 'Latex');
L = legend([h1, h3], ...
    'mean of fans\_fans', ...
    'mean of fans\_friends', ...
    'location', 'NE');
set(L, 'FontSize', 12, 'box', 'off');
set(gca, 'FontSize', 18);
set(gca, 'LineWidth', 2);
set(gcf,'color','white');
set(gcf, 'Position', [600 400 700 500]);





