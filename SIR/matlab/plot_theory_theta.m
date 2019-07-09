function plot_theory_theta(theta)

ha = tight_subplot(2, 1, [.1 .1],[.1 .05],[.15 .1]);
set(gcf,'color','white');
set(gcf, 'Position', [600 100 500 700]);
set(gcf, 'PaperPositionMode', 'auto');

k = cell2mat(struct2cell(load('./data/ki_bj.mat'))); k = k(k~=0);
left = (ceil(theta.*k)-1) ./ k; right = ceil(theta.*k) ./ k;
Ptheta=(left+right)/2;
[counts, centers]=hist(Ptheta,20);
axes(ha(1));
bar(centers, counts/sum(counts), 'FaceColor', 'b', 'EdgeColor', 'b');
ylabel('Distribution');
xlim([0.05 0.3]); ylim([0 0.45]);
set(gca, 'FontName', 'Times New Roman', 'FontSize', 18); 
set(gca, 'LineWidth', 2);

axes(ha(2));
x=0:0.05:0.3; y=[0 0 0 0 1 0 0];
plot(x, y, 'm-', 'LineWidth', 3);
xlim([0.05 0.3]);
xlabel('\theta');
ylabel('Precision');
set(gca, 'FontName', 'Times New Roman', 'FontSize', 18); 
set(gca, 'LineWidth', 2);

