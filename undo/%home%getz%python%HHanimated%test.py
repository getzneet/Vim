Vim�UnDo� @���RȚ����`�B��H9I�گE~8b_6Q   $   plt.plot(x, y(x), color="red")                             ZT�     _�                            ����                                                                                                                                                                                                                                                                                                                                                             ZT�[     �                /bins = np.arange(-100, 100, 1) # fixed bin size5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ZT�[     �                .bins = np.arange(100, 100, 1) # fixed bin size5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ZT�[     �                -bins = np.arange(00, 100, 1) # fixed bin size5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ZT�[     �                ,bins = np.arange(0, 100, 1) # fixed bin size5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ZT�\     �                # fixed bin size�                +bins = np.arange(, 100, 1) # fixed bin size5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ZT�a     �                ,bins = np.arange(0, 100, 1) # fixed bin size5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ZT�a     �                # fixed bin size�                )bins = np.arange(0, , 1) # fixed bin size5�_�      	                     ����                                                                                                                                                                                                                                                                                                                                                             ZT�g     �                %#plt.xlim([min(data)-5, max(data)+5])�                plt.xlim(-5,50)5�_�      
           	           ����                                                                                                                                                                                                                                                                                                                                                             ZT�l    �                plt.ylim(0,60)5�_�   	              
           ����                                                                                                                                                                                                                                                                                                                                                             ZT��     �                 �             5�_�   
                         ����                                                                                                                                                                                                                                                                                                                                                             ZT��     �                 �              5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ZT��     �         !      (from scipy.stats.kde import gaussian_kde5�_�                    
        ����                                                                                                                                                                                                                                                                                                                                                             ZT��     �   
      !    �   
      !    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ZT��     �         "    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ZT��     �         #       �         #    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ZT��     �                 5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ZT��     �                 5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ZT��    �                 �         $       5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ZT��    �                 �         $      plt.plot(x, y(x))5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ZT��     �         $      y = gaussian_kde(data)5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ZT��     �         $       = gaussian_kde(data)5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ZT��     �         $      plt.plot(x, y(x), color="red")5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ZT��    �                 �         $      plt.plot(x, (x), color="red")5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ZT��     �         $    �         $      %x = np.linspace(min(data), max(data))   y = gaussian_kde(data)        5��