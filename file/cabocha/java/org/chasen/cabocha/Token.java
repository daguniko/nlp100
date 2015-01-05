/* ----------------------------------------------------------------------------
 * This file was automatically generated by SWIG (http://www.swig.org).
 * Version 2.0.4
 *
 * Do not make changes to this file unless you know what you are doing--modify
 * the SWIG interface file instead.
 * ----------------------------------------------------------------------------- */

package org.chasen.cabocha;

public class Token {
  private long swigCPtr;
  protected boolean swigCMemOwn;

  public Token(long cPtr, boolean cMemoryOwn) {
    swigCMemOwn = cMemoryOwn;
    swigCPtr = cPtr;
  }

  public static long getCPtr(Token obj) {
    return (obj == null) ? 0 : obj.swigCPtr;
  }

  public synchronized void delete() {
    if (swigCPtr != 0) {
      if (swigCMemOwn) {
        swigCMemOwn = false;
        throw new UnsupportedOperationException("C++ destructor does not have public access");
      }
      swigCPtr = 0;
    }
  }

  public String getSurface() {
    return CaboChaJNI.Token_surface_get(swigCPtr, this);
  }

  public String getNormalized_surface() {
    return CaboChaJNI.Token_normalized_surface_get(swigCPtr, this);
  }

  public String getFeature() {
    return CaboChaJNI.Token_feature_get(swigCPtr, this);
  }

  public int getFeature_list_size() {
    return CaboChaJNI.Token_feature_list_size_get(swigCPtr, this);
  }

  public String getNe() {
    return CaboChaJNI.Token_ne_get(swigCPtr, this);
  }

  public String getAdditional_info() {
    return CaboChaJNI.Token_additional_info_get(swigCPtr, this);
  }

  public Chunk getChunk() {
    long cPtr = CaboChaJNI.Token_chunk_get(swigCPtr, this);
    return (cPtr == 0) ? null : new Chunk(cPtr, false);
  }

  public String feature_list(long i) {
    return CaboChaJNI.Token_feature_list(swigCPtr, this, i);
  }

}
