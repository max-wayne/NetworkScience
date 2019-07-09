function plot_empirical_theta()

ha = tight_subplot(2, 1, [.1 .1],[.1 .05],[.15 .1]);
set(gcf,'color','white');
set(gcf, 'Position', [600 100 500 700]);
set(gcf, 'PaperPositionMode', 'auto');

t = 'D:/Projects/Pycharm/SIR/data/55/4166087832403843/res/retweet_see_k';  % 实证信息
% t = 'D:/Projects/Pycharm/SIR/data/55/4166087832403843/meme_simu/m1/retweet_see_k';  % 模拟SIR
% t = 'D:/Projects/Pycharm/SIR/master/data/simu_weibo/beijing/simu_lt_time/5p0_01/m2/retweet_see_k_1';  % 模拟LT
d = load(t); left = d(:, 2) - 1; right = d(:, 2); ki = d(:, 3);
theta_left = left./ki; theta_right = right./ki;
theta = (left./ki+right./ki) / 2; tbl = tabulate(theta); x = tbl(:, 1);

axes(ha(1));
[counts, centers] = hist(x, 20);
bar(centers, counts/sum(counts), 'FaceColor', [0, 0.45, 0.74], 'EdgeColor', [0, 0.45, 0.74]);
% hold on;
% plot([0.1 0.1], [0 0.3], 'r--', 'LineWidth', 2);
ylabel('Distribution');
xlim([0 0.5]); ylim([0 0.3]);
set(gca, 'FontName', 'Times New Roman', 'FontSize', 18); 
set(gca, 'LineWidth', 2);

%{
figure;
boxplot(theta);
ylabel('$\theta$', 'interpreter', 'latex');
set(gca, 'FontName', 'Times New Roman', 'FontSize', 15); 
set(gca, 'LineWidth', 2);
set(gcf,'color','white');
set(gcf, 'Position', [600 400 700 500]);
%}
p1 = []; p2 = []; theta_min = min(theta); theta_max = max(theta);
interval = (theta_max-theta_min) / 500; x = theta_min+interval : interval : theta_max;
for theta_0 = theta_min+interval : interval : theta_max
    r1 = find(theta_0>theta_left&theta_0<=theta_right); p1 = [p1 length(r1)/length(d)];
%     section_left = theta_0 - fluc * theta_0;
%     section_right = theta_0 + fluc * theta_0;
%     r2 = find(section_right<=theta_left|section_left>theta_right);
%     p2 = [p2 1-length(r2)/length(d)]; 
end

axes(ha(2));
plot(x, p1, '-','Color', [0, 0.5, 0], 'Linewidth', 3);
xlim([0 0.5]);
% hold on;
% plot([0.1 0.1], [0 1], 'r--', 'LineWidth', 2);
xlabel('\theta');
ylabel('Precision');
set(gca, 'FontName', 'Times New Roman', 'FontSize', 18); 
set(gca, 'LineWidth', 2);
%{
figure;
plot(x, p2, '-','Color', [0.87, 0.49, 0], 'Linewidth', 3);
xlabel(['$\theta_{0}\pm\theta_{0}*$', num2str(fluc)], 'interpreter', 'latex');
ylabel('$Precision$', 'interpreter', 'latex');
set(gca, 'FontName', 'Times New Roman', 'FontSize', 15); 
set(gca, 'LineWidth', 2);
set(gcf,'color','white');
set(gcf, 'Position', [600 400 700 500]);
%}

