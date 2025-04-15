import express from "express";
import * as turmasController from "../controllers/turmasController.js";

const router = express.Router();

router.get("/", turmasController.getTurmas);
router.get("/data", turmasController.getTurmasByDate);
router.get("/pagination", turmasController.getTurmasPagination);
router.get("/:id", turmasController.getTurmasById);

router.post("/adicionar", turmasController.addTurmas);

router.delete("/delete/:id", turmasController.deleteTurma);

router.put("/patch/:id", turmasController.patchTurma);
router.put("/graduar/:id", turmasController.graduateTurma);

export default router;
