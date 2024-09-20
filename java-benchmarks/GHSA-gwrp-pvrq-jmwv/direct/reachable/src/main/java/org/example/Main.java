package org.example;

import org.apache.commons.io.FilenameUtils;

public class Main {
  public static void main(String[] args) {
    String hello = FilenameUtils.normalize("Hello world!");
    System.out.println(hello);
  }
}