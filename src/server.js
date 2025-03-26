import app from "./app.js";

app.use((err, req, res, next) => {
  console.log(err.stack);
  res.status(500).send("Somehting broke");
});

app.get("/", (req, res) => {
  return res.status(200).send("Server Working");
});

app.listen(8080, () => {
  console.log("Server running at 8080");
});
