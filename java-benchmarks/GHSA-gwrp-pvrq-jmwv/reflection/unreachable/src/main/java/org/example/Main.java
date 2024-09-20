package org.example;

import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;

public class Main {
  public static void main(String[] args) {
    try {
      Class<?> cls = Class.forName("org.example.DoesNotExist");
      Method m = cls.getDeclaredMethod("normalize", String.class);
      Object res = m.invoke(null, "I'm vulnerable!");
      System.out.println(res);
    } catch (ClassNotFoundException | NoSuchMethodException | IllegalAccessException |
             InvocationTargetException e) {
      throw new RuntimeException(e);
    }
  }
}