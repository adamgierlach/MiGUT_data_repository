%% Main script to run for power analysis of MiGUT (figure 2d)
%% Written By: Adam Gierlach
%% Last Modified: 2024-02-26

%% Battery Life

% Plotting vars
title_font_size = 14;
label_font_size = 14;
tick_font_size = 12;

programmed_sps = [62.5, 125, 250, 500, 1000, 2000, 4000, 8000];

stream_power = [6.7, 7.41, 8.88, 11.66, 16.47, 23.03, 23.41, 23.06]-(6.7-6.28); %mA

sleep_power = 6e-6;
dutycycle = linspace(0, 1, 100)';

current_traces = dutycycle*stream_power + (1-dutycycle)*sleep_power*ones(size(stream_power))
battery_capacity = 23

battery_life = battery_capacity ./ current_traces';

fig2_power = figure();
ax1 = gca;

plot(dutycycle, battery_life, 'LineWidth',1.5);
xlabel("Transmit and record to sleep ratio", 'FontSize',label_font_size,'FontWeight','bold');
ylabel("Battery life (hours)", 'FontSize',label_font_size,'FontWeight','bold')

l = legend(string(programmed_sps))
title(l, "Sampling Rate (SPS)")
l.Title.FontSize = 12;
l.FontSize = 12;
ax1.XAxis.FontSize = tick_font_size;
ax1.YAxis.FontSize = tick_font_size;

ylim([0,24*2])

saveas(fig2_power, "main_fig2_power3.bmp")






















