/*
 * Copyright LWJGL. All rights reserved.
 * License terms: http://lwjgl.org/license.php
 * MACHINE GENERATED FILE, DO NOT EDIT
 */
package org.lwjgl.opengles;

/**
 * Native bindings to the <a href="https://www.khronos.org/registry/gles/extensions/KHR/blend_equation_advanced.txt">KHR_blend_equation_advanced_coherent</a> extension.
 * 
 * <p>This extension guarantees that blending is done coherently and in API primitive order. An enable is provided to allow implementations to opt out of
 * fully coherent blending and instead behave as though only {@link KHRBlendEquationAdvanced KHR_blend_equation_advanced} were supported.</p>
 * 
 * <p>Requires {@link GLES20 GLES 2.0} and {@link EXTBlendMinmax EXT_blend_minmax}.</p>
 */
public final class KHRBlendEquationAdvancedCoherent {

	/**
	 * Accepted by the {@code cap} parameter of Disable, Enable, and IsEnabled, and by the {@code pname} parameter of GetIntegerv, GetBooleanv, GetFloatv,
	 * GetDoublev and GetInteger64v.
	 */
	public static final int GL_BLEND_ADVANCED_COHERENT_KHR = 0x9285;

	private KHRBlendEquationAdvancedCoherent() {}

}