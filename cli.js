#!/usr/bin/env node

const program = require("commander");
const cyberpun = require("./index");

program
  .version("1.0.0", "-v, --version")
  .option("-l, --list", "List all the jokes");

program.on("--help", () => {
  console.log("  Examples:");
  console.log("");
  console.log("    $ cyberpun");
  console.log("    $ cyberpun --list");
  console.log("    $ cyberpun -l");
  console.log("");
});

program.parse(process.argv);

console.log(program.list ? cyberpun.list().join("\n") : cyberpun.random());
