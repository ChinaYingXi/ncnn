
find_package(Python3 REQUIRED COMPONENTS Interpreter)

macro(pnnx_add_test name)
    add_test(NAME test_${name} COMMAND ${CMAKE_COMMAND} -DPYTHON_EXECUTABLE=${Python3_EXECUTABLE} -DPYTHON_SCRIPT=${CMAKE_CURRENT_SOURCE_DIR}/test_${name}.py -P ${CMAKE_CURRENT_SOURCE_DIR}/run_test.cmake)
endmacro()

pnnx_add_test(F_adaptive_avg_pool1d)
pnnx_add_test(F_adaptive_avg_pool2d)
pnnx_add_test(F_adaptive_avg_pool3d)
pnnx_add_test(F_adaptive_max_pool1d)
pnnx_add_test(F_adaptive_max_pool2d)
pnnx_add_test(F_adaptive_max_pool3d)
pnnx_add_test(F_alpha_dropout)
pnnx_add_test(F_affine_grid)
pnnx_add_test(F_avg_pool1d)
pnnx_add_test(F_avg_pool2d)
pnnx_add_test(F_avg_pool3d)
pnnx_add_test(F_batch_norm)
pnnx_add_test(F_celu)
pnnx_add_test(F_conv1d)
pnnx_add_test(F_conv2d)
pnnx_add_test(F_conv3d)
pnnx_add_test(F_conv_transpose1d)
pnnx_add_test(F_conv_transpose2d)
pnnx_add_test(F_conv_transpose3d)
pnnx_add_test(F_dropout)
pnnx_add_test(F_dropout2d)
pnnx_add_test(F_dropout3d)
pnnx_add_test(F_elu)
pnnx_add_test(F_embedding)
pnnx_add_test(F_feature_alpha_dropout)
pnnx_add_test(F_fold)
pnnx_add_test(F_gelu)
pnnx_add_test(F_glu)
pnnx_add_test(F_grid_sample)
pnnx_add_test(F_group_norm)
pnnx_add_test(F_hardshrink)
pnnx_add_test(F_hardsigmoid)
pnnx_add_test(F_hardswish)
pnnx_add_test(F_hardtanh)
pnnx_add_test(F_instance_norm)
pnnx_add_test(F_interpolate)
pnnx_add_test(F_layer_norm)
pnnx_add_test(F_leaky_relu)
pnnx_add_test(F_linear)
pnnx_add_test(F_local_response_norm)
pnnx_add_test(F_log_softmax)
pnnx_add_test(F_logsigmoid)
pnnx_add_test(F_lp_pool1d)
pnnx_add_test(F_lp_pool2d)
pnnx_add_test(F_max_pool1d)
pnnx_add_test(F_max_pool2d)
pnnx_add_test(F_max_pool3d)
pnnx_add_test(F_mish)
pnnx_add_test(F_normalize)
pnnx_add_test(F_pad)
pnnx_add_test(F_pairwise_distance)
pnnx_add_test(F_pixel_shuffle)
pnnx_add_test(F_pixel_unshuffle)
pnnx_add_test(F_prelu)
pnnx_add_test(F_relu)
pnnx_add_test(F_relu6)
pnnx_add_test(F_rms_norm)
pnnx_add_test(F_rrelu)
pnnx_add_test(F_scaled_dot_product_attention)
pnnx_add_test(F_selu)
pnnx_add_test(F_sigmoid)
pnnx_add_test(F_silu)
pnnx_add_test(F_softmax)
pnnx_add_test(F_softmin)
pnnx_add_test(F_softplus)
pnnx_add_test(F_softshrink)
pnnx_add_test(F_softsign)
pnnx_add_test(F_tanh)
pnnx_add_test(F_tanhshrink)
pnnx_add_test(F_threshold)
pnnx_add_test(F_unfold)
pnnx_add_test(F_upsample_bilinear)
pnnx_add_test(F_upsample_nearest)
pnnx_add_test(F_upsample)

pnnx_add_test(nn_AdaptiveAvgPool1d)
pnnx_add_test(nn_AdaptiveAvgPool2d)
pnnx_add_test(nn_AdaptiveAvgPool3d)
pnnx_add_test(nn_AdaptiveMaxPool1d)
pnnx_add_test(nn_AdaptiveMaxPool2d)
pnnx_add_test(nn_AdaptiveMaxPool3d)
pnnx_add_test(nn_AlphaDropout)
pnnx_add_test(nn_AvgPool1d)
pnnx_add_test(nn_AvgPool2d)
pnnx_add_test(nn_AvgPool3d)
pnnx_add_test(nn_BatchNorm1d)
pnnx_add_test(nn_BatchNorm2d)
pnnx_add_test(nn_BatchNorm3d)
pnnx_add_test(nn_CELU)
pnnx_add_test(nn_ChannelShuffle)
pnnx_add_test(nn_ConstantPad1d)
pnnx_add_test(nn_ConstantPad2d)
pnnx_add_test(nn_ConstantPad3d)
pnnx_add_test(nn_Conv1d)
pnnx_add_test(nn_Conv2d)
pnnx_add_test(nn_Conv3d)
pnnx_add_test(nn_ConvTranspose1d)
pnnx_add_test(nn_ConvTranspose2d)
pnnx_add_test(nn_ConvTranspose3d)
pnnx_add_test(nn_Dropout)
pnnx_add_test(nn_Dropout2d)
pnnx_add_test(nn_Dropout3d)
pnnx_add_test(nn_ELU)
pnnx_add_test(nn_Embedding)
pnnx_add_test(nn_Fold)
pnnx_add_test(nn_GELU)
pnnx_add_test(nn_GLU)
pnnx_add_test(nn_GroupNorm)
pnnx_add_test(nn_GRU)
pnnx_add_test(nn_Hardshrink)
pnnx_add_test(nn_Hardsigmoid)
pnnx_add_test(nn_Hardswish)
pnnx_add_test(nn_Hardtanh)
pnnx_add_test(nn_Identity)
pnnx_add_test(nn_InstanceNorm1d)
pnnx_add_test(nn_InstanceNorm2d)
pnnx_add_test(nn_InstanceNorm3d)
pnnx_add_test(nn_LayerNorm)
pnnx_add_test(nn_LeakyReLU)
pnnx_add_test(nn_Linear)
pnnx_add_test(nn_LocalResponseNorm)
pnnx_add_test(nn_LogSigmoid)
pnnx_add_test(nn_LogSoftmax)
pnnx_add_test(nn_LPPool1d)
pnnx_add_test(nn_LPPool2d)
pnnx_add_test(nn_LSTM)
pnnx_add_test(nn_MaxPool1d)
pnnx_add_test(nn_MaxPool2d)
pnnx_add_test(nn_MaxPool3d)
pnnx_add_test(nn_Mish)
pnnx_add_test(nn_MultiheadAttention)
pnnx_add_test(nn_PixelShuffle)
pnnx_add_test(nn_PixelUnshuffle)
pnnx_add_test(nn_PReLU)
pnnx_add_test(nn_ReflectionPad1d)
pnnx_add_test(nn_ReflectionPad2d)
pnnx_add_test(nn_ReLU)
pnnx_add_test(nn_ReLU6)
pnnx_add_test(nn_ReplicationPad1d)
pnnx_add_test(nn_ReplicationPad2d)
pnnx_add_test(nn_ReplicationPad3d)
pnnx_add_test(nn_RMSNorm)
pnnx_add_test(nn_RNN)
pnnx_add_test(nn_RReLU)
pnnx_add_test(nn_SELU)
pnnx_add_test(nn_Sigmoid)
pnnx_add_test(nn_SiLU)
pnnx_add_test(nn_Softmax)
pnnx_add_test(nn_Softmax2d)
pnnx_add_test(nn_Softmin)
pnnx_add_test(nn_Softplus)
pnnx_add_test(nn_Softshrink)
pnnx_add_test(nn_Softsign)
pnnx_add_test(nn_Tanh)
pnnx_add_test(nn_Tanhshrink)
pnnx_add_test(nn_Threshold)
pnnx_add_test(nn_Unfold)
pnnx_add_test(nn_Upsample)
pnnx_add_test(nn_UpsamplingBilinear2d)
pnnx_add_test(nn_UpsamplingNearest2d)
pnnx_add_test(nn_ZeroPad2d)

pnnx_add_test(Tensor_contiguous)
pnnx_add_test(Tensor_expand)
pnnx_add_test(Tensor_fill)
pnnx_add_test(Tensor_index)
pnnx_add_test(Tensor_index_put)
pnnx_add_test(Tensor_masked_fill)
pnnx_add_test(Tensor_new_empty)
pnnx_add_test(Tensor_new_full)
pnnx_add_test(Tensor_new_ones)
pnnx_add_test(Tensor_new_zeros)
pnnx_add_test(Tensor_permute)
pnnx_add_test(Tensor_repeat)
pnnx_add_test(Tensor_reshape)
pnnx_add_test(Tensor_select)
pnnx_add_test(Tensor_slice)
pnnx_add_test(Tensor_slice_copy)
pnnx_add_test(Tensor_to)
pnnx_add_test(Tensor_type_as)
pnnx_add_test(Tensor_view)

pnnx_add_test(torch_addmm)
pnnx_add_test(torch_amax)
pnnx_add_test(torch_amin)
pnnx_add_test(torch_arange)
pnnx_add_test(torch_argmax)
pnnx_add_test(torch_argmin)
pnnx_add_test(torch_bitwise_not)
pnnx_add_test(torch_bitwise_and)
pnnx_add_test(torch_bitwise_or)
pnnx_add_test(torch_bitwise_xor)
pnnx_add_test(torch_bitwise_left_shift)
pnnx_add_test(torch_bitwise_right_shift)
pnnx_add_test(torch_bmm)
pnnx_add_test(torch_cat)
pnnx_add_test(torch_chunk)
pnnx_add_test(torch_clone)
pnnx_add_test(torch_complex)
pnnx_add_test(torch_cross)
pnnx_add_test(torch_cumprod)
pnnx_add_test(torch_cumsum)
pnnx_add_test(torch_einsum)
pnnx_add_test(torch_eq)
pnnx_add_test(torch_diag)
pnnx_add_test(torch_flatten)
pnnx_add_test(torch_full)
pnnx_add_test(torch_full_like)
pnnx_add_test(torch_gather)
pnnx_add_test(torch_ge)
pnnx_add_test(torch_gt)
pnnx_add_test(torch_index_select)
pnnx_add_test(torch_le)
pnnx_add_test(torch_lgamma)
pnnx_add_test(torch_logical_not)
pnnx_add_test(torch_logical_and)
pnnx_add_test(torch_logical_or)
pnnx_add_test(torch_logical_xor)
pnnx_add_test(torch_logsumexp)
pnnx_add_test(torch_lt)
pnnx_add_test(torch_masked_select)
pnnx_add_test(torch_matmul)
pnnx_add_test(torch_max)
pnnx_add_test(torch_mean)
pnnx_add_test(torch_min)
pnnx_add_test(torch_mm)
pnnx_add_test(torch_mv)
pnnx_add_test(torch_narrow)
pnnx_add_test(torch_ne)
pnnx_add_test(torch_norm)
pnnx_add_test(torch_ones)
pnnx_add_test(torch_ones_like)
pnnx_add_test(torch_positive)
pnnx_add_test(torch_prod)
pnnx_add_test(torch_repeat_interleave)
pnnx_add_test(torch_roll)
pnnx_add_test(torch_scatter_add)
pnnx_add_test(torch_slice_scatter)
pnnx_add_test(torch_sum)
pnnx_add_test(torch_split)
pnnx_add_test(torch_squeeze)
pnnx_add_test(torch_stack)
pnnx_add_test(torch_std)
pnnx_add_test(torch_t)
pnnx_add_test(torch_tensor_split)
pnnx_add_test(torch_tile)
pnnx_add_test(torch_topk)
pnnx_add_test(torch_transpose)
pnnx_add_test(torch_unbind)
pnnx_add_test(torch_unsqueeze)
pnnx_add_test(torch_view_as_complex)
pnnx_add_test(torch_view_as_real)
pnnx_add_test(torch_where)
pnnx_add_test(torch_zeros)
pnnx_add_test(torch_zeros_like)

pnnx_add_test(torch_stft)
pnnx_add_test(torch_istft)

pnnx_add_test(torch_fft_irfft)
pnnx_add_test(torch_fft_irfft2)
pnnx_add_test(torch_fft_irfftn)
pnnx_add_test(torch_fft_rfft)
pnnx_add_test(torch_fft_rfft2)
pnnx_add_test(torch_fft_rfftn)

pnnx_add_test(torch_fft_ihfft)
pnnx_add_test(torch_fft_ihfft2)
pnnx_add_test(torch_fft_ihfftn)
pnnx_add_test(torch_fft_hfft)
pnnx_add_test(torch_fft_hfft2)
pnnx_add_test(torch_fft_hfftn)

pnnx_add_test(torch_fft_ifft)
pnnx_add_test(torch_fft_ifft2)
pnnx_add_test(torch_fft_ifftn)
pnnx_add_test(torch_fft_fft)
pnnx_add_test(torch_fft_fft2)
pnnx_add_test(torch_fft_fftn)

pnnx_add_test(torch_abs)
pnnx_add_test(torch_acos)
pnnx_add_test(torch_acosh)
pnnx_add_test(torch_asin)
pnnx_add_test(torch_asinh)
pnnx_add_test(torch_atan)
pnnx_add_test(torch_atanh)
pnnx_add_test(torch_atan2)
pnnx_add_test(torch_ceil)
pnnx_add_test(torch_clamp)
pnnx_add_test(torch_cos)
pnnx_add_test(torch_cosh)
pnnx_add_test(torch_exp)
pnnx_add_test(torch_floor)
pnnx_add_test(torch_imag)
pnnx_add_test(torch_log)
pnnx_add_test(torch_log10)
pnnx_add_test(torch_logaddexp)
pnnx_add_test(torch_maximum)
pnnx_add_test(torch_minimum)
pnnx_add_test(torch_neg)
pnnx_add_test(torch_pow)
pnnx_add_test(torch_real)
pnnx_add_test(torch_reciprocal)
pnnx_add_test(torch_round)
pnnx_add_test(torch_rsqrt)
pnnx_add_test(torch_sign)
pnnx_add_test(torch_sin)
pnnx_add_test(torch_sinh)
pnnx_add_test(torch_sqrt)
pnnx_add_test(torch_square)
pnnx_add_test(torch_tan)
pnnx_add_test(torch_tanh)
pnnx_add_test(torch_trunc)

pnnx_add_test(convnext_tiny)
pnnx_add_test(mobilenet_v2)
pnnx_add_test(mobilenet_v3_small)
pnnx_add_test(resnet18)
pnnx_add_test(shufflenet_v2_x1_0)
pnnx_add_test(squeezenet1_1)
pnnx_add_test(swin_t)
pnnx_add_test(vit_b_32)

pnnx_add_test(ir_complex)

# TODO enable end2end quantization model test
#pnnx_add_test(quantization_shufflenet_v2_x1_0)

pnnx_add_test(pnnx_eliminate_noop_cat)
pnnx_add_test(pnnx_eliminate_noop_expand)
pnnx_add_test(pnnx_eliminate_noop_math)
pnnx_add_test(pnnx_eliminate_noop_upsample)
pnnx_add_test(pnnx_expression)
pnnx_add_test(pnnx_fold_constant)
pnnx_add_test(pnnx_fuse_conv1d_batchnorm1d)
pnnx_add_test(pnnx_fuse_conv2d_batchnorm2d)
pnnx_add_test(pnnx_fuse_conv3d_batchnorm3d)
pnnx_add_test(pnnx_fuse_convtranspose1d_batchnorm1d)
pnnx_add_test(pnnx_fuse_convtranspose2d_batchnorm2d)
pnnx_add_test(pnnx_fuse_convtranspose3d_batchnorm3d)
pnnx_add_test(pnnx_fuse_input_unpack)
pnnx_add_test(pnnx_fuse_layernorm)
pnnx_add_test(pnnx_fuse_linear_batchnorm1d)
pnnx_add_test(pnnx_fuse_multiheadattention)
pnnx_add_test(pnnx_fuse_rmsnorm)
pnnx_add_test(pnnx_fuse_scaled_dot_product_attention)
pnnx_add_test(pnnx_fuse_select_to_unbind)
pnnx_add_test(pnnx_fuse_slice_to_tensor_split)
pnnx_add_test(pnnx_fuse_adjacent_reshape)
pnnx_add_test(pnnx_fuse_pad_conv1d)
pnnx_add_test(pnnx_fuse_pad_conv2d)
pnnx_add_test(pnnx_fuse_pixel_unshuffle)

if(TorchVision_FOUND)
    pnnx_add_test(torchvision_DeformConv2d)
    pnnx_add_test(torchvision_RoIAlign)
endif()

pnnx_add_test(torchaudio_F_inverse_spectrogram)
pnnx_add_test(torchaudio_F_spectrogram)
pnnx_add_test(torchaudio_InverseSpectrogram)
pnnx_add_test(torchaudio_Spectrogram)

pnnx_add_test(transformers_albert_attention)
pnnx_add_test(transformers_bart_attention)
pnnx_add_test(transformers_bert_attention)
pnnx_add_test(transformers_bert_generation_attention)
pnnx_add_test(transformers_blenderbot_attention)
pnnx_add_test(transformers_camembert_attention)
pnnx_add_test(transformers_clip_attention)
pnnx_add_test(transformers_chinese_clip_attention)
pnnx_add_test(transformers_ctrl_attention)
pnnx_add_test(transformers_deberta_attention)
pnnx_add_test(transformers_distilbert_attention)
pnnx_add_test(transformers_electra_attention)
pnnx_add_test(transformers_flaubert_attention)
pnnx_add_test(transformers_fsmt_attention)
pnnx_add_test(transformers_funnel_attention)
pnnx_add_test(transformers_gpt2_attention)
pnnx_add_test(transformers_layoutlm_attention)
pnnx_add_test(transformers_longformer_attention)
pnnx_add_test(transformers_lxmert_attention)
pnnx_add_test(transformers_marian_attention)
pnnx_add_test(transformers_mbart_attention)
pnnx_add_test(transformers_mobilebert_attention)
pnnx_add_test(transformers_mt5_attention)
pnnx_add_test(transformers_openai_attention)
pnnx_add_test(transformers_pegasus_attention)
pnnx_add_test(transformers_prophetnet_attention)
pnnx_add_test(transformers_reformer_attention)
pnnx_add_test(transformers_roberta_attention)
pnnx_add_test(transformers_squeezebert_attention)
pnnx_add_test(transformers_t5_attention)
pnnx_add_test(transformers_xlm_attention)
pnnx_add_test(transformers_xlm_roberta_attention)
pnnx_add_test(transformers_xlnet_attention)

add_subdirectory(ncnn)

if(onnxruntime_FOUND)
    add_subdirectory(onnx)
endif()
