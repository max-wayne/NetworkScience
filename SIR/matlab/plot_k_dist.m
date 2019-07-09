function plot_k_dist()

ha = tight_subplot(1, 2,[.1 .1],[.1 .05],[.1 .1]);
set(gcf,'color','white');
set(gcf, 'Position', [500 200 1000 600]);
set(gcf, 'PaperPositionMode', 'auto');

axes(ha(1));
load('D:\Projects\Pycharm\SIR\data\info_stat\Ki_dist');
ki=Ki_dist(:,1); p1=Ki_dist(:,2);
h1=semilogx(ki, p1, '-o', 'MarkerSize', 8);
hold on;
mu=3; sigma=1;
y=0.01*exp(-(log(ki)-mu).^2./sigma^2/2);
h2=semilogx(ki, y, 'r--', 'LineWidth', 2);
xlabel('The number of friends'); 
ylabel('Distribution');
legend([h1 h2], {'Ki', '\mu=3, \sigma=1'});
set(gca, 'FontName', 'TimesNewRoman', 'FontSize', 12, 'LineWidth', 1.5);
set(legend, 'box', 'off', 'FontName', 'Times New Roman', 'FontSize', 15);

axes(ha(2));
load('D:\Projects\Pycharm\SIR\data\info_stat\Ko_dist');
ko=Ko_dist(:,1); p2=Ko_dist(:,2);
h3=loglog(ko, p2, '-o', 'Color', [0 0.75 0.75], 'MarkerSize', 8);
hold on; 
h4=plot([1e2 1e4], [1e-2 1e-6], 'k--', 'LineWidth', 2);
xlabel('The number of followers'); 
legend([h3 h4], {'Ko', '\gamma=2'});
ylim([1e-9 1]);
set(gca, 'FontName', 'TimesNewRoman', 'FontSize', 12, 'LineWidth', 1.5);
set(legend, 'box', 'off', 'FontName', 'Times New Roman', 'FontSize', 15);


