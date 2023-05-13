from scipy.interpolate import UnivariateSpline, InterpolatedUnivariateSpline
import numpy as np

def get_piecewise_warping(beta, fs):
    low_cut_off = 300
    high_cut_off = 5500
    beta_low = beta ** 2
    F_low = low_cut_off * beta_low
    F_high = F_low + beta * (high_cut_off - low_cut_off)
    beta_high = ((fs/2) - F_high) / ((fs / 2) - high_cut_off)
    def fn(f):
        if f <= low_cut_off:
            return beta_low * f
        elif f <= high_cut_off:
            return F_low + beta * (f - low_cut_off)
        else:
            return F_high + beta_high * (f - high_cut_off)
    return  fn


def get_linear_warping(alpha, fs):
    def fn(f):
        return f*alpha
    return fn


def transform(sp, alpha, fs, warping='linear'):
    N, D = sp.shape
    sp_out = sp[:]
    
    half_fft = D - 1
    f = np.arange(half_fft + 1)[1:] / half_fft * (fs // 2)
    if warping == 'linear':
        warping_fn = get_linear_warping(alpha, fs)
    elif warping == 'piecewise':
        warping_fn = get_piecewise_warping(alpha, fs)
    
    f_alpha = np.zeros(f.shape)
    for i in range(len(f)):
        f_alpha[i] = warping_fn(f[i])

    for frame_i in range(N):
        sp_i = sp[frame_i][1:]
        fn = InterpolatedUnivariateSpline(f_alpha, sp_i)
        shifted_sp_i = fn(f)

        sp_out[frame_i][1:] = shifted_sp_i
        
    return sp_out



        
