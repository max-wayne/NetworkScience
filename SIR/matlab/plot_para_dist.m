function plot_para_dist(bin)
%% plot beta1, a, b distribution.
load('D:\double_check\info\stat_results\beta1_a_b_2017_trunc10');
% beta1
figure(); beta_1 = para(:, 1);
[m, n] = hist(beta_1, bin);
semilogx(n, m./sum(m), '--o');
xlabel('$\beta_{1}$', 'interpreter', 'LaTeX');
ylabel('$Dist$', 'interpreter', 'LaTeX');
% a
figure(); a = para(:, 2); idx = a~=1;
[m, n] = hist(a(idx), bin);
plot(n, m/length(a), '--o');
xlabel('$a$', 'interpreter', 'LaTeX');
ylabel('$Dist$', 'interpreter', 'LaTeX');
% b
figure(); b = para(:, 3); 
[m, n] = hist(b(idx), bin);
plot(n, m/length(b), '--o');
xlabel('$b$', 'interpreter', 'LaTeX');
ylabel('$Dist$', 'interpreter', 'LaTeX');

