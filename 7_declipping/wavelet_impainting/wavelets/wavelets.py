import numpy as np

def get_wavelet_filter(name, param):
    """This is a collection of wavelet filters transfered from 
    numerical tours implementations for matlab. Supporting limited 
    numbers of options. 
    
    Source: toolbox_signal/compute_wavelet_filter.m
    """
    if name == 'Daubechies':
        supported_params = (4, 6, 8, 10, 20)
        if param not in supported_params:
            raise TypeError(f"Supported params for {name}: {supported_params}")
        if param == 4:
            f = [.482962913145, .836516303738, .224143868042, -.129409522551]
        if param == 6:
            f = [.332670552950, .806891509311, .459877502118, -.135011020010,
                 -.085441273882, .035226291882]
        if param == 8:
            f = [.230377813309, .714846570553,
                 .630880767930, -.027983769417,
                 -.187034811719, .030841381836,
                 .032883011667, -.010597401785]
        if param == 10:
            f = [.160102397974, .603829269797, .724308528438,
                .138428145901, -.242294887066, -.032244869585,
                .077571493840, -.006241490213, -.012580751999, .003335725285]
        if param == 20:
            f = [.026670057901, .188176800078, .527201188932,
                .688459039454, .281172343661, -.249846424327,
                -.195946274377, .127369340336, .093057364604,
                -.071394147166, -.029457536822, .033212674059,
                .003606553567, -.010733175483, .001395351747,
                .001992405295, -.000685856695, -.000116466855,
                .000093588670, -.000013264203]
            
    if name == 'Coiflet':
        supported_params = (2, )
        if param not in supported_params: 
            raise TypeError(f"Supported params for {name}: {supported_params}")
        if param == 2:
            f = [.016387336463, -.041464936782, -.067372554722,
                 .386110066823, .812723635450, .417005184424,
                 -.076488599078, -.059434418646, .023680171947,
                 .005611434819, -.001823208871, -.000720549445]
    if name == 'Symmlet':
        supported_params = (4, )
        if param not in supported_params:
            raise TypeError(f"Supported params for {name}: {supported_params}")
        if param == 4:
            f = [ -.107148901418, -.041910965125, .703739068656,
                 1.136658243408, .421234534204, -.140317624179,
                 -.017824701442, .045570345896]

    return np.array([0] + f)
