%% Main script to run for communication analysis of MiGUT (figure 2e)
%% Written By: Adam Gierlach
%% Last Modified: 2024-02-26


% import file ../data/2022.10.03_day00.txt and name output table as data03 
% remember to update the datetime for the realtime column

close all

title_font_size = 14;
label_font_size = 14;
tick_font_size = 12;

FS = 62.5;
minutes_avg = 1;
sample_avg = minutes_avg*(62.5*60);
rssi_avg = movmean(data03.rssi, sample_avg);

fig2 = figure()
ax1 = subplot(2,1,2)
hold all

%plot(data03.realtime, data03.rssi, "*-")
plot(data03.timestamps/60, rssi_avg, "k-", 'LineWidth',1.5);


%yline(mean(data03.rssi), 'g', 'LineWidth',2)

title({""}, "FontSize",title_font_size);
xlabel("Time (minutes)", "FontSize",label_font_size, 'FontWeight','bold')
ylabel({"RSSI (dBm)"}, "FontSize",label_font_size, 'FontWeight','bold')
ax1.XAxis.FontSize = tick_font_size;
ax1.YAxis.FontSize = tick_font_size;

% Plot bounding lines
cc1310_sensitivity = -97;
benchtop_rssi = -20;

yline(benchtop_rssi,'k--' ,'LineWidth',1.5)
yline(cc1310_sensitivity,'k-.' ,'LineWidth',1.5)

legend(["Ingested Device RSSI", "Benchtop Device RSSI", "Device Sensitivity"])%, 'Position',[0.598809529663551,0.765958016186648,0.287499994145972,0.108333330459538]);



FS = 62.5;
minutes_avg = 20/60;
sample_avg = minutes_avg*(FS*60);

data_diff = diff(data03.packet);
data_diff1 = data_diff(data_diff > 0);
data_diff2 = data_diff1 -1;
diff_mean = movmean(data_diff2, sample_avg);
num_packets_in_sample_avg = sample_avg/FS;

xlim([0, 45])

% yyaxis right
% plot(data03.timestamps/60, [0; 0; 0; missed_packets_time]/total_packets*100, 'r', 'LineWidth',1.5);
% ylabel("Percentage of missed packets (%)");
% ylim([0, 1.2])
ax2 = subplot(2,1,1)
plot(data03.timestamps(1:end-1)/60, 100-[0; 0; 0; diff_mean]/num_packets_in_sample_avg*100, 'g', 'LineWidth',1.5);
%title("Data Loss during Experiment","FontSize",title_font_size)
xlim([0, 45])

ylabel({"Packets";" recieved (%)"},"FontSize",label_font_size, 'FontWeight','bold');
%ylim([0, 1.2])
%xlabel("Time (minutes)", "FontSize",label_font_size, 'FontWeight','bold')

eat = [2 3.5; 4.5 5; 7 10; 11 11.5;15 21.75;24 38.7;40 41.75; 44 45;45.75 46]-3
move = [3.5 4.5; 5 7; 10 11; 11.5 13;21.75 24;38.7 40; 41.75 43; 45 44.5; 46 48]-3
sleep = [13 15]-3
play = [43 44; 44.5 45.75]-3
activity_y_value = 100.5;
activity_width = 5;
for i = 1:size(eat, 1) % Feeding
    line(eat(i,:), [activity_y_value, activity_y_value], 'HandleVisibility','off', 'LineWidth', activity_width, 'Color', '#548235');
end
for i = 1:size(move, 1) % Ambulation
    line(move(i,:), [activity_y_value, activity_y_value], 'HandleVisibility','off', 'LineWidth', activity_width, 'Color', '#2F5597');
end
for i = 1:size(sleep, 1) % Napping
    line(sleep(i,:), [activity_y_value, activity_y_value], 'HandleVisibility','off', 'LineWidth', activity_width, 'Color', '#FFC000');
end
for i = 1:size(play, 1) % Playing
    line(play(i,:), [activity_y_value, activity_y_value], 'HandleVisibility','off', 'LineWidth', activity_width, 'Color', '#A2142F');
end

ax2.XAxis.FontSize = tick_font_size;
ax2.YAxis.FontSize = tick_font_size;

linkaxes([ax1 ax2], 'x')
xlim([0, 45])

ylim([97, 100.5])


saveas(fig2, "fig2_rssi.pdf")
