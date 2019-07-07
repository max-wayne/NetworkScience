clear; clc;
load('D:\double_check\info\stat_results\interim_res');
beta_x = ones(337, 200) * 2; trunc = 200;
for i = 1 : 337
    for j = 1 :200
        if interim_res_fenmu(i, j) >= trunc
            beta_x(i, j) = interim_res_fenzi(i, j) / interim_res_fenmu(i, j);
        end
    end
end
%% Plot
beta_x_avg = zeros(200, 1);
for k = 1 : 200
    idx = find(beta_x(:, k)~=2);
    beta_x_avg(k) = mean(beta_x(idx, k));
end
plot(beta_x_avg, '-o');
xlabel('$ReceivedTime$', 'Interpreter', 'LaTeX');
ylabel('$\beta_{x}$', 'Interpreter', 'LaTeX');
set(gcf,'color','white');
set(gcf, 'Position', [600 280 600 500]);
set(gca, 'FontName', 'Times New Roman', 'FontSize', 20);
