package org.example;

import org.apache.struts2.dispatcher.HttpParameters;
import org.apache.struts2.dispatcher.Parameter;

public class Main {
  public static void main(String[] args) {
  }

  public Parameter get(HttpParameters httpParameters, Object key) {
    return httpParameters.get(key);
  }
}