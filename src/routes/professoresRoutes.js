import express from "express";
import * as professoresController from "../controllers/professoresController.js";

const router = express.Router();

router.get("/", professoresController.getProfessores);
router.get("/:id", professoresController.getProfessoresById);

router.post("/adicionar", professoresController.addProfessores);

export default router;
